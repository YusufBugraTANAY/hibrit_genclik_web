import React from 'react';
import { Swiper, SwiperSlide } from 'swiper/react';
import { Autoplay, Pagination, EffectFade } from 'swiper/modules';

import 'swiper/css';
import 'swiper/css/pagination';
import 'swiper/css/effect-fade';

export default function NewsCarousel({ projects, lang = 'tr' }) {
  const isTr = lang === 'tr';
  
  return (
    <div className="w-full relative">
      <Swiper
        modules={[Autoplay, Pagination, EffectFade]}
        spaceBetween={30}
        slidesPerView={1}
        breakpoints={{
          640: { slidesPerView: 1 },
          768: { slidesPerView: 2 },
          1024: { slidesPerView: 3 },
        }}
        autoplay={{ delay: 3000, disableOnInteraction: false }}
        pagination={{ clickable: true, dynamicBullets: true }}
        className="pb-16"
      >
        {projects.map((project) => (
          <SwiperSlide key={project.id} className="h-auto">
            <div className="glass-card h-full flex flex-col overflow-hidden group cursor-pointer transition-transform duration-300 hover:-translate-y-2">
              <div className="aspect-video relative overflow-hidden bg-slate-100 border-b border-slate-200">
                {/* Fallback pattern */}
                <div className="absolute inset-0 opacity-20 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-mint via-slate-100 to-slate-100 z-0"></div>
                <div className="absolute inset-0 flex items-center justify-center text-slate-400 z-0">
                  <span className="font-semibold text-xl tracking-widest uppercase opacity-20">{project.category}</span>
                </div>
                
                {/* Actual Image */}
                {project.image && (
                  <img 
                    src={project.image} 
                    alt={project.title[lang] || project.title.tr} 
                    className="absolute inset-0 w-full h-full object-cover z-10 group-hover:scale-105 transition-transform duration-500"
                    onError={(e) => e.target.style.display = 'none'}
                  />
                )}
                <div className="absolute inset-0 bg-gradient-to-t from-white to-transparent opacity-90 z-20"></div>
              </div>
              <div className="p-6 flex-grow flex flex-col">
                <div className="flex items-center gap-3 mb-4">
                  <span className="text-xs font-bold text-primary-dark bg-mint/20 px-3 py-1 rounded-full border border-mint/30">
                    {project.category}
                  </span>
                  <span className="text-xs text-slate-500 font-medium">
                    {new Date(project.date).toLocaleDateString(isTr ? 'tr-TR' : 'en-US', { month: 'short', year: 'numeric' })}
                  </span>
                </div>
                <h3 className="text-xl font-bold text-slate-deep mb-3 line-clamp-1 group-hover:text-primary transition-colors">
                  {project.title[lang] || project.title.tr}
                </h3>
                <p className="text-sm text-slate-text line-clamp-2 leading-relaxed flex-grow">
                  {project.summary[lang] || project.summary.tr}
                </p>
                
                <a href={isTr ? `/projeler/${project.slug}/` : `/en/projeler/${project.slug}/`} className="mt-6 inline-flex items-center text-sm font-semibold text-primary hover:text-primary-dark transition-colors group/link">
                  {isTr ? 'Detaylı İncele' : 'View Details'}
                  <svg className="w-4 h-4 ml-1 transform group-hover/link:translate-x-1 transition-transform" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
                </a>
              </div>
            </div>
          </SwiperSlide>
        ))}
      </Swiper>
    </div>
  );
}
